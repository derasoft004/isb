#include <iostream>
#include <cstdlib>
#include <ctime>

void generateRandomBitArray(int bitArray[], int size) {
    srand(time(nullptr)); // Устанавливаем начальное значение для генератора случайных чисел

    for (int i = 0; i < size; i++) {
        bitArray[i] = rand() % 2; // Генерируем случайное число 0 или 1
    }
}

int main() {
    const int SIZE = 128;
    int randomBitArray[SIZE];

    generateRandomBitArray(randomBitArray, SIZE);

    // Выводим сгенерированный массив на экран
    for (int i = 0; i < SIZE; i++) {
        std::cout << randomBitArray[i];
    }

    return 0;
}