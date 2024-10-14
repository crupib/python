#include <iostream>
#include <chrono>

int main() {
    // Start the timer
    auto start = std::chrono::high_resolution_clock::now();

    // Counting loop
    unsigned long long count = 0;
    for (unsigned long long i = 0; i < 1'000'000'000; ++i) {
        ++count;
    }

    // Stop the timer
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time in seconds
    std::chrono::duration<double> elapsed = end - start;

    // Output the result
    std::cout << "Time taken to count to one billion: " << elapsed.count() << " seconds\n";

    return 0;
}

