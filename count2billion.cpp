#include <iostream>
#include <chrono>  // For timing

int main() {
    // Start the timer using chrono
    auto start = std::chrono::high_resolution_clock::now();

    // Loop to count to one billion
    unsigned long long count = 0;
    for (unsigned long long i = 0; i < 1000000000; ++i) {
        count++;
    }

    // Stop the timer
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate the duration
    std::chrono::duration<double> elapsed = end - start;

    // Output the elapsed time in seconds
    std::cout << "Time taken to count to one billion: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}

