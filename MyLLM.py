import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def generate_code(input_text):
    print("Hello World")

    # Load pre-trained model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Set the model to evaluation mode
    model.eval()

    # Input text
    # input_text = "write a code in c# for hello world program."

    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1,
                                early_stopping=True, temperature=0.7)

    # Decode and print generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Generated text:")
    print(generated_text)

def generate_code(input_text):
    # Load pre-trained model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Set the model to evaluation mode
    model.eval()

    # Input text (code-related prompt)
    # input_text = """
    #     // Java code to generate a random number between 1 and 100
    #     import java.util.Random;
    #
    #     public class RandomNumberGenerator {
    #         public static void main(String[] args) {
    #             Random random = new Random();
    #             int randomNumber = random.nextInt(100) + 1;
    #             System.out.println("Random number: " + randomNumber);
    #         }
    #     }
    #     """

    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate code
    with torch.no_grad():
        output = model.generate(input_ids, max_length=500, num_return_sequences=1,
                                early_stopping=True, temperature=0.7)

    # Decode and print generated code
    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Generated code:")
    print(generated_code)


if __name__ == "__main__":
    # generate_code("write a code in c# for hello world program.")

    input_text = """
        // Java code to generate a random number between 1 and 100
        import java.util.Random;

        public class RandomNumberGenerator {
            public static void main(String[] args) {
                Random random = new Random();
                int randomNumber = random.nextInt(100) + 1;
                System.out.println("Random number: " + randomNumber);
            }
        }
        """
    generate_code(input_text)

