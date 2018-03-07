import crypt
import os
import getpass
from subprocess import call

collected_random=""
count = 0
things_to_collect="desires/wishes/hopes/dreams/random whatevers"
gender_ct={'m': 0, 'f': 0, 'o': 0}

print(count)

def collect(sssh):
  global count, collected_random
  print(sssh)
  sha_desires=crypt.crypt(sssh, crypt.mksalt(crypt.METHOD_SHA512))
  print(" adding %s and %s " % (collected_random, sha_desires))
  collected_random=crypt.crypt(collected_random + sha_desires, crypt.mksalt(crypt.METHOD_SHA512))
  os.system('clear')
  print("  **yay!** Your secret %s will be mixed into zcash!!" % things_to_collect)
 # print(collected_random)

def run_powers_of_tau(secret_mix):
  global count
  print
  print
  print("*" * 80)
#  print("  Running Powers of Tau with secret mix %s from %s humans." % (secret_mix, count))
  pot_cmd="""cargo run --release --bin compute <<EOD
  %s
  EOD""" % secret_mix
  os.system(pot_cmd)
  print
  print

def collect_stats():
  file = open("round-stats.txt","w") 
  file.write("male %s; " % gender_ct['m'])
  file.write("female %s; " % gender_ct['f'])
  file.write("other %s " % gender_ct['o'])
  file.close()

status=""
while(status != "done"):
  count = count + 1
  gender=input(" Enter m, f, o (other): ")
  if(gender=="m" or gender=="f" or gender=="o"):
     gender_ct[gender] = gender_ct[gender] + 1

  desire = getpass.getpass("  What are your %s number %s? " % (things_to_collect, count))
  collect(desire)
  status=getpass.getpass("  Hit enter to move to the next person, or 'done' to run PoT")
  os.system('clear')

collect_stats()
run_powers_of_tau(collected_random)
