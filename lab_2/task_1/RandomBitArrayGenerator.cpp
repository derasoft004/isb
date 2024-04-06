#include <iostream>
#include <cstdlib>
#include <ctime>


void generateRandomBitArray(int bitArray[], int size) {
    /**
     * Generates a random bit array of a given size.
     *
     * @param bitArray bit array to fill with random values.
     * @param size size of the bit array.
    */
    srand(time(nullptr)); // Set the seed for the random number generator

    for (int i = 0; i < size; i++) {
        bitArray[i] = rand() % 2; // Generate a random number 0 or 1
    }
}


int main() {
    /**
     * Demonstrates the use of the generateRandomBitArray function to generate a random bit array of
     * length 128 and prints it to the console.
     *
     * @return 0 on success.
     */
    const int SIZE = 128;
    int randomBitArray[SIZE];

    generateRandomBitArray(randomBitArray, SIZE);

    // Print the generated bit array to the console
    for (int i = 0; i < SIZE; i++) {
        std::cout << randomBitArray[i];
    }

    return 0;
}