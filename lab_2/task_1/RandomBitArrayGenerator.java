import java.util.Random;

public class RandomBitArrayGenerator {

    public static void main(String[] args) {
        int[] randomBitArray = generateRandomBitArray(128);

        for (int i = 0; i < randomBitArray.length; i++) {
            System.out.print(randomBitArray[i]);
        }
    }

    public static int[] generateRandomBitArray(int size) {
        Random random = new Random();
        int[] bitArray = new int[size];

        for (int i = 0; i < size; i++) {
            bitArray[i] = random.nextInt(2); // Генерируем случайное число 0 или 1
        }

        return bitArray;
    }
}