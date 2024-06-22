#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def measure_runtime(start_time):
    """Calculate and print the total elapsed runtime."""
    end_time = time.time()
    elapsed_time = end_time - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"\n** Total Elapsed Runtime: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")

def main():
    start_time = time.time()
    
    # Parse command-line arguments
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)
    
    # Get pet labels
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)
    
    # Classify images
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)
    
    # Adjust results for is-a-dog
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)
    
    # Calculate results statistics
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)
    
    # Print final results
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Measure and print total runtime
    measure_runtime(start_time)

if __name__ == "__main__":
    main()
