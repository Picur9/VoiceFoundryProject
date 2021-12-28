import sys
import time
import vanity
import vanity_advance

def main(argv):
    start = time.perf_counter()
    resp = vanity.generate(argv)
    end = time.perf_counter()
    print(f"Vanity numbers for {argv}:", *resp)
    print(f"Generation took {end - start:0.4f} seconds")
 
    start = time.perf_counter()
    resp = vanity_advance.generate(argv)
    end = time.perf_counter()
    print(f"Vanity advance numbers for {argv}:", *resp)
    print(f"Generation took {end - start:0.4f} seconds")

if __name__ == "__main__":
   main(sys.argv[1])
