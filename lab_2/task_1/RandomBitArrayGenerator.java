public class RandomBitArrayGenerator {

    /**
     * Generates a random bit array of a given size.
     *
     * @param size size of the bit array.
     * @return random bit array.
     */
    public static int[] generateRandomBitArray(int size) {
        Random random = new Random();
        int[] bitArray = new int[size];

        for (int i = 0; i < size; i++) {
            bitArray[i] = random.nextInt(2); // Generate a random number 0 or 1
        }

        return bitArray;
    }

    /**
     * Demonstrates the use of the generateRandomBitArray(int size)
     * method to generate a random bit array of length 128 and prints it to the console.
     *
     * @param args command line arguments.
     */
    public static void main(String[] args) {
        int[] randomBitArray = generateRandomBitArray(128);

        for (int i = 0; i < randomBitArray.length; i++) {
            System.out.print(randomBitArray[i]);
        }
    }
}