package recfun
import common._

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0) 1 else {
      if (c == r) 1 else {
        pascal(c - 1, r - 1) + pascal(c, r - 1)
      }
    }
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def countPar(lc: Int, rc: Int, chars: List[Char]): Boolean = {
      if (rc > lc) false else {
        if (chars.isEmpty && rc == lc) true else {
          if (chars.isEmpty && rc != lc) false else {
            if (chars.head == "("(0)) countPar(lc + 1, rc, chars.tail) else {
              if (chars.head == ")"(0)) countPar(lc, rc + 1, chars.tail) else {
                countPar(lc, rc, chars.tail)
              }
            }
          }
        }
      }
    }
    countPar(0, 0, chars: List[Char])
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0) 1 else {
      if (money < 0 || coins.isEmpty) 0 else {
        countChange(money, coins.tail) + countChange(money - coins.head, coins)
      }
    }
  } 
}
