
import requests, sys, json

# input file provided as sys.argv[1] element
with open(sys.argv[1]) as f:
    list_of_hits = [line.rstrip('\n') for line in f]

# Helper function to download data
def get_url(url, **kwargs):
  response = requests.get(url, **kwargs);

  if not response.ok:
    print(response.text)
    response.raise_for_status()
    sys.exit()

  return response

def get_uniprot_seq(uniprot_id):
  uniprot_id = uniprot_id.split("_")[0]

  # Documentation: https://www.uniprot.org/help/api
  WEBSITE_API = "https://rest.uniprot.org/"

  # all of the entry as an example
  r = get_url(f"{WEBSITE_API}/uniprotkb/%s?fields=sequence" %uniprot_id)
  data = r.json()
  ## get the sequence
  seq_str = data['sequence']['value']

  return(seq_str)


def get_motif_hits(re_str, seq_str):
    ## search the motif of interest
    import regex as re
    list_hits = re.findall(re_str, seq_str, overlapped=True)
    
    ## get hits index as a dictionary
    string_hits_dict = {k: seq_str.index(k)+1 for k in list_hits}
    return(string_hits_dict)


## N-glycosilation motif
re_str = "N[^P][ST][^P]"

for i in list_of_hits:
    res_i = get_motif_hits(re_str=re_str, seq_str=get_uniprot_seq(i))

    if len(res_i.values())>0:
        print(i)
        motif_str_hits = "\t".join(map(str, res_i.values()))
        print(motif_str_hits)