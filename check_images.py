import argparse
from time import time, sleep
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    # Measure total program runtime by collecting start time
    start_time = time()

    # Get command line arguments
    in_arg = get_input_args()

    # Get pet image labels
    results = get_pet_labels(in_arg.dir)

    # Get classification results
    classify_images(in_arg.dir, results, in_arg.arch)

    # Adjust results for is-a-dog/not-a-dog classification
    adjust_results4_isadog(results, in_arg.dogfile)

    # Calculate results statistics
    results_stats = calculates_results_stats(results)

    # Print results
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Print total time to run
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:", str(int(tot_time / 3600)) + ":" + 
          str(int((tot_time % 3600) / 60)) + ":" + 
          str(int((tot_time % 3600) % 60)) )

if __name__ == "__main__":
    main()
