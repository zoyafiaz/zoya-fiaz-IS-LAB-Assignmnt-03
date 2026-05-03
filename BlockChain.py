import hashlib
import datetime

# -----------------------------
# Block Class
# -----------------------------
class Block:

    def __init__(self, index, timestamp, data, previous_hash):

        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        # Calculate hash of current block
        self.hash = self.calculate_hash()

    # Function to calculate SHA256 hash
    def calculate_hash(self):

        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash)
        )

        return hashlib.sha256(block_string.encode()).hexdigest()


# -----------------------------
# Blockchain Class
# -----------------------------
class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis_block()]

    # Create first block
    def create_genesis_block(self):

        return Block(
            0,
            datetime.datetime.now(),
            "Genesis Block",
            "0"
        )

    # Get latest block
    def get_latest_block(self):

        return self.chain[-1]

    # Add new block
    def add_block(self, new_block):


        new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)

    # Display blockchain
    def display_chain(self):

        for block in self.chain:

            print("\n-------------------------")
            print("Block Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)

    # Verify blockchain integrity
    def is_chain_valid(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate hash
            if current_block.hash != current_block.calculate_hash():

                return False

            # Compare previous hash
            if current_block.previous_hash != previous_block.hash:

                return False

        return True


# -----------------------------
# Main Program
# -----------------------------

# Create blockchain
my_blockchain = Blockchain()

# Add blocks
my_blockchain.add_block(
    Block(1, datetime.datetime.now(), "Ali sends 5 BTC to Ahmed", "")
)

my_blockchain.add_block(
    Block(2, datetime.datetime.now(), "Ahmed sends 2 BTC to Sara", "")
)

my_blockchain.add_block(
    Block(3, datetime.datetime.now(), "Sara sends 1 BTC to Zoya", "")
)

my_blockchain.add_block(
    Block(4, datetime.datetime.now(), "Zoya sends 3 BTC to Hamza", "")
)

# Display blockchain
print("\n========= ORIGINAL BLOCKCHAIN =========")
my_blockchain.display_chain()

# Validate blockchain
print("\nIs Blockchain Valid?", my_blockchain.is_chain_valid())

# -----------------------------------------
# Modify one block to show blockchain effect
# -----------------------------------------

print("\n\n========= MODIFYING BLOCK 2 =========")

my_blockchain.chain[2].data = "Ahmed sends 100 BTC to Sara"

# Recalculate modified block hash
my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()

# Display blockchain again
my_blockchain.display_chain()

# Validate again
print("\nIs Blockchain Valid After Modification?",
      my_blockchain.is_chain_valid())