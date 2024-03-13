from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils  import BlockhainUtils
import pprintpp

if __name__ == '__main__':
    amount = 1
    type = 'TRANSFER'
    sender = 'sender'
    reciever = 'reciever'
    
    wallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(reciever, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    
    blockchain = Blockchain()
    # blockchain.addBlock(block)

    lastHash = BlockhainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)
    if not (blockchain.lastBlockHashValid(block)):
        print("Last Block hash not valid")
    if not (blockchain.blockCountValid(block)):
        print("Block count not valid")
    if (blockchain.lastBlockHashValid(block)) and (blockchain.blockCountValid(block)):
        blockchain.addBlock(block)


    print(blockchain.toJson())