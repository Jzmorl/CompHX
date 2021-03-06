#!/usr/bin/env python3

import HX_analyze as hx
import HX_boundary_cond as bc
import sys
import matplotlib.pyplot as plt

# This script works as an example of how to use the modules developed to solve a HX problem with provided boundary conditions

def main():
    """ This file is set up to run an example simulation of a finned and tubed heat exchanger for both counter flow and parallel flow.
    
    The results are plotted in scatter plots and saved to file for each HX type. 
    """
    
    name = sys.argv[1]
#    name = "input.yaml"
    
    
    hot_temp_in, hot_temp_out, cold_temp_in, cold_temp_out = bc.set_temp_boundary_conditions(name)
    
    h_cold, area_cold, h_hot, area_hot = bc.set_flow_boundary_conditions(name)

    
    q_fin_counter, fin_counter_vars = hx.q_fin(hx.log_mean_temp_diff_counter(hot_temp_in, hot_temp_out, cold_temp_in, cold_temp_out),name)
    q_fin_parallel, fin_parallel_vars = hx.q_fin(hx.log_mean_temp_diff_parallel(hot_temp_in, hot_temp_out, cold_temp_in, cold_temp_out),name)
    
    q_tube_counter, tube_counter_vars = hx.q_tube(hx.log_mean_temp_diff_counter(hot_temp_in, hot_temp_out, cold_temp_in, cold_temp_out),name)
    q_tube_parallel, tube_parallel_vars = hx.q_tube(hx.log_mean_temp_diff_parallel(hot_temp_in, hot_temp_out, cold_temp_in, cold_temp_out),name)
    
    max_counter_fin = []
    max_parallel_fin = []
    
    max_counter_tube = []
    max_parallel_tube = []
    
    
    
    for i in range(len(q_fin_counter)):
        if q_fin_counter[i] == max(q_fin_counter):
            max_counter_fin.append(fin_counter_vars[i])
        if q_fin_parallel[i] == max(q_fin_parallel):
            max_parallel_fin.append(fin_parallel_vars[i])
            
    
    for i in range(len(q_tube_counter)):
        if q_tube_counter[i] == max(q_tube_counter):
            max_counter_tube.append(tube_counter_vars[i])
        if q_tube_parallel[i] == max(q_tube_parallel):
            max_parallel_tube.append(tube_parallel_vars[i])
            
    print(max(q_fin_counter))
    print(max(q_fin_parallel))
    print(max(q_tube_counter))
    print(max(q_tube_parallel))
    
    print(max_counter_fin)
    print(max_parallel_fin)
    print(max_counter_tube)
    print(max_parallel_tube)
    
            
    
    plt.scatter(range(len(q_fin_counter)), q_fin_counter, label = "Finned Counter-Flow")
    plt.title('Finned Counter-Flow')
    plt.xlabel('Input Variable Permutations')
    plt.ylabel('Heat Rate (W)')
    plt.legend()
    plt.savefig("q_fin_counter.png")
    plt.show()
    plt.close()
    
    plt.scatter(range(len(q_fin_parallel)), q_fin_parallel, label = "Finned Parallel Flow")
    plt.title('Finned Parallel Flow')
    plt.xlabel('Input Variable Permutations')
    plt.ylabel('Heat Rate (W)')
    plt.legend()
    plt.savefig("q_fin_parallel.png")
    plt.show()
    plt.close()
    
    plt.scatter(range(len(q_tube_counter)), q_tube_counter, label = "Tubed Counter-Flow")
    plt.title('Tubed Counter-Flow')
    plt.xlabel('Input Variable Permutations')
    plt.ylabel('Heat Rate (W)')
    plt.legend()
    plt.savefig("q_tube_counter.png")
    plt.show()
    plt.close()
    
    plt.scatter(range(len(q_tube_parallel)), q_tube_parallel, label = "Tubed Parallel Flow")
    plt.title('Tubed Parallel-Flow')
    plt.xlabel('Input Variable Permutations')
    plt.ylabel('Heat Rate (W)')
    plt.legend()
    plt.savefig("q_tube_parallel.png")
    plt.show()
    plt.close()
    

if __name__ == "__main__":
    main()