import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Membuat hash SHA-256 dari seluruh properti blok.
        Menggunakan json.dumps dengan sort_keys=True agar urutan data konsisten.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mekanisme Proof of Work: 
        Mencari hash yang diawali dengan sejumlah '0' sesuai difficulty.
        """
        target = "0" * difficulty
        start_time = time.time()
        
        print(f"   ⛏️  Mining Block #{self.index} (Difficulty: {difficulty})...")
        
        # Loop Brute Force: Coba terus nonce sampai hash memenuhi target
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
        end_time = time.time()
        print(f"   ✅ Block Mined! Hash: {self.hash}")
        print(f"      Nonce: {self.nonce} | Time: {end_time - start_time:.4f} sec")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        # Difficulty 4 artinya Hash harus diawali "0000"
        # Semakin tinggi angka ini, semakin lama mining-nya.
        self.difficulty = 4 

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block (Ilham's Chain)")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # 1. Ambil hash dari blok terakhir sebagai referensi (Linking)
        new_block.previous_hash = self.get_latest_block().hash
        # 2. Lakukan proses Mining (Proof of Work)
        new_block.mine_block(self.difficulty)
        # 3. Masukkan blok yang sudah valid ke dalam rantai
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Memeriksa integritas seluruh blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Cek 1: Apakah hash block saat ini valid (sesuai kalkulasi ulang)?
            if current_block.hash != current_block.calculate_hash():
                print(f"❌ Invalid Hash at Block {i}")
                return False

            # Cek 2: Apakah previous_hash cocok dengan hash blok sebelumnya?
            if current_block.previous_hash != previous_block.hash:
                print(f"❌ Broken Link between Block {i-1} and {i}")
                return False
                
        return True

# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("      TINYCHAIN: BLOCKCHAIN SIMULATION (PoW)")
    print("      Nama : Mochamad Ilham Hansyil Alfauzi")
    print("      NIM  : 2320202767")
    print("="*60 + "\n")

    my_chain = Blockchain()

    # Skenario: Menambahkan Blok Transaksi
    print("[INFO] Menambahkan Blok 1 (Transaksi A -> B)...")
    my_chain.add_block(Block(1, "", {"sender": "Ilham", "receiver": "Dosen", "amount": 100}))
    print("-" * 60)

    print("[INFO] Menambahkan Blok 2 (Transaksi B -> C)...")
    my_chain.add_block(Block(2, "", {"sender": "Dosen", "receiver": "Kampus", "amount": 50}))
    print("-" * 60)

    print("[INFO] Menambahkan Blok 3 (Transaksi C -> A)...")
    my_chain.add_block(Block(3, "", {"sender": "Kampus", "receiver": "Ilham", "amount": 10}))
    print("\n" + "="*60)

    # Validasi Akhir
    print(f"Status Validitas Blockchain: {'VALID' if my_chain.is_chain_valid() else 'INVALID'}")
    
    # Menampilkan isi rantai
    print("\n[INFO] Isi Blockchain:")
    for block in my_chain.chain:
        print(f"Index: {block.index} | Nonce: {block.nonce} | Hash: {block.hash}")

    print("="*60)