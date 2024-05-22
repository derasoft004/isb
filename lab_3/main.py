import argparse

from hybrid_system import HybridSystem
from symmetric_algorithm import SymmetricAlgorithm
from asymmetric_algorithm import AsymmetricAlgorithm
from file_util import *
from constants import PATHS


@func_handler
def argparser():
    """
    parses command line arguments and returns the parsed arguments as a Namespace object.
    """
    parser = argparse.ArgumentParser()

    paths_default = FileAssistant(PATHS)
    paths_dict = paths_default.read_json_file()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--keys',
                       action='store_true',
                       help='Run key generation mode.')
    group.add_argument('-enc', '--encryption',
                       action='store_true',
                       help='Run encryption mode.')
    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode.')

    parser.add_argument('-len', '--key_length',
                        type=int,
                        default=448,
                        help='Length of the symmetric key in bits (default: 448)')

    parser.add_argument('-text', '--input_text_file',
                        type=str,
                        default=paths_dict["text_file"],
                        help='Path of the input txt file with text (default: "data/message.txt")')

    parser.add_argument('-public_key', '--public_key_path',
                        type=str,
                        default=paths_dict["public_key"],
                        help='Path of the public pem file with key (default: "data/public.pem")')

    parser.add_argument('-private_key', '--private_key_path',
                        type=str,
                        default=paths_dict["private_key"],
                        help='Path of the private pem file with key (default: "data/private.pem")')

    parser.add_argument('-sym_key', '--symmetric_key_path',
                        type=str,
                        default=paths_dict["symmetric_key_file"],
                        help='Path of the symmetric txt file with key (default: "data/symmetric_448.txt")')

    parser.add_argument('-enc_path', '--encrypted_text_path',
                        type=str,
                        default=paths_dict["encrypted_text_file"],
                        help='Path of the txt file with encrypted text (default: "data/encrypted_text.txt")')

    parser.add_argument('-dec_path', '--decrypted_text_path',
                        type=str,
                        default=paths_dict["decrypted_text_file"],
                        help='Path of the txt file with decrypted text (default: "data/decrypted_text.txt")')

    args = parser.parse_args()

    if args.key_length not in list(range(32, 448+1, 8)):
        raise argparse.ArgumentTypeError

    return args


@func_handler
def main():
    args = argparser()

    symmetric_crypto = SymmetricAlgorithm(args.key_length)
    asymmetric_crypto = AsymmetricAlgorithm(args.private_key_path, args.public_key_path)
    operator = HybridSystem(args.input_text_file,
                            args.symmetric_key_path, args.encrypted_text_path,
                            args.decrypted_text_path, symmetric_crypto, asymmetric_crypto)

    match args:
        case args if args.keys:
            operator.generate_keys()

        case args if args.encryption:
            operator.encrypt_text()

        case args if args.decryption:
            operator.decrypt_text()


if __name__ == "__main__":
    main()
