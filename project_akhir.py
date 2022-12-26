def main():
# The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # Fungsi yang digunakan untuk memulai permainan.

def intro():
# Fungsi ini memperkenalkan aturan permainan Tic Tac Toe
    print("Halo! Selamat datang di game")
    print("________ __                   ________                          ________              ____  ____", 
      "\n\__  __/|__|  _____           \__  __/_______    _____          \__  __/ ___    ____  |  |  |  |",
      "\n  |  |   __  /  ___\   ____     |  |   \__   \  /  ___\   ____    |  |  / _ \  / __ \ |  |  |  |", 
      "\n  |  |  |  | \  \     /___/     |  |     / __ \ \  \     /___/    |  | / / \ \(  ___/  \/    \/", 
      "\n  |  |  |  |  \  \__            |  |    / /__/ \ \  \__           |  | \ \_/ / \ \__   __    __", 
      "\n  |__|  |__|   \_____\          |__|   (________) \____\          |__|  \___/   \___) |__|  |__|")
    print("\n")
    print("Aturan: Pemain 1 dan pemain 2, diwakili oleh X dan O, bergiliran "
          "menandai ruang dalam kisi 3*3. Pemain yang berhasil menempatkan "
          "tiga tanda mereka dalam baris horizontal, vertikal, atau diagonal menang.")
    print("\n")
    input("Tekan enter untuk melanjutkan.")
    print("\n")

def create_grid():
# Fungsi ini membuat playboard kosong
    print("Ini papan permainannya: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def sym():
# Fungsi ini menentukan simbol pemain
    symbol_1 = input("Pemain 1, apakah Anda ingin menjadi X atau O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Pemain 2, kamu adalah O. ")
    else:
        symbol_2 = "X"
        print("Pemain 2, Anda adalah X. ")
    input("Tekan enter untuk melanjutkan.")
    print("\n")
    return (symbol_1, symbol_2)

def startGamming(board, symbol_1, symbol_2, count):
# Fungsi ini memulai permainan.

    # Memutuskan giliran
    if count % 2 == 0:
        pemain = symbol_1
    elif count % 2 == 1:
        pemain = symbol_2
    print("Pemain "+ pemain + ", giliran Anda. ")
    baris = int(input("Pilih satu baris:"
                    "[baris atas: masukkan 0, baris tengah: masukkan 1, baris bawah: masukkan 2]:"))
    kolom = int(input("Pilih kolom:"
                       "[kolom kiri: masukkan 0, kolom tengah: masukkan 1, kolom kanan masukkan 2]"))


    # Periksa apakah pilihan pemain di luar jangkauan
    while (baris > 2 or baris < 0) or (kolom > 2 or kolom < 0):
        outOfBoard(baris, kolom)
        baris = int(input("Pilih satu baris[baris atas:"
                        "[masukkan 0, baris tengah: masukkan 1, baris bawah: masukkan 2]:"))
        kolom = int(input("Pilih kolom:"
                           "[kolom kiri: masukkan 0, kolom tengah: masukkan 1, kolom kanan masukkan 2]"))

        # Periksa apakah kotak sudah terisi
    while (board[baris][kolom] == symbol_1)or (board[baris][kolom] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, baris, kolom)
        baris = int(input("Pilih satu baris[baris atas:"
                        "[masukkan 0, baris tengah: masukkan 1, baris bawah: masukkan 2]:"))
        kolom = int(input("Pilih kolom:"
                            "[kolom kiri: masukkan 0, kolom tengah: masukkan 1, kolom kanan masukkan 2]"))    
        
    # Menempatkan simbol pemain di papan tulis
    if pemain == symbol_1:
        board[baris][kolom] = symbol_1
            
    else:
        board[baris][kolom] = symbol_2
    
    return (board)

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# Fungsi ini memeriksa apakah papan sudah penuh
    while count < 10 and winner == True:
        game = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("Papan penuh. Permainan telah berakhir.")
            if winner == True:
                print("There is a tie. ")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Permainan telah berakhir.")
        
    # Ini adalah fungsi memberikan laporan 
    report(count, winner, symbol_1, symbol_2)

def outOfBoard(baris, kolom):
# Fungsi ini memberi tahu para pemain bahwa pilihan mereka berada di luar jangkauan
    print("Di luar jangkauan. Pilih yang lain. ")

def printPretty(board):
# Fungsi ini mencetak papan dengan bagus!
    baris = len(board)
    kolom = len(board)
    print("---+---+---")
    for r in range(baris):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def isWinner(board, symbol_1, symbol_2, count):
# Fungsi ini memeriksa apakah ada pemenang yang menang
    winner = True
    # Memeriksa baris-baris
    for baris in range (0, 3):
        if (board[baris][0] == board[baris][1] == board[baris][2] == symbol_1):
            winner = False
            print("Pemain " + symbol_1 + ", kamu menang!")
   
        elif (board[baris][0] == board[baris][1] == board[baris][2] == symbol_2):
            winner = False
            print("Pemain " + symbol_2 + ", kamu menang!")
            
            
    # Memeriksan kolom-kolom
    for kolom in range (0, 3):
        if (board[0][kolom] == board[1][kolom] == board[2][kolom] == symbol_1):
            winner = False
            print("Pemain " + symbol_1 + ", kamu menang!")
        elif (board[0][kolom] == board[1][kolom] == board[2][kolom] == symbol_2):
            winner = False
            print("Pemain " + symbol_2 + ", kamu menang!")

    # Memeriksa diagonal-diagonal
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Pemain " + symbol_1 + ", kamu menang!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Pemain " + symbol_2 + ", kamu menang!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Pemain " + symbol_1 + ", kamu menang!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Pemain " + symbol_2 + ", kamu menang!")

    return winner

def illegal(board, symbol_1, symbol_2, row, column):
    print("Kotak yang Anda pilih sudah terisi. Pilih yang lain.")

def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Tekan enter untuk melihat ringkasan game. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Pemain " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Pemain " + symbol_2 + ".")
    else:
        print("There is a tie. ")

# Call Main
main()
