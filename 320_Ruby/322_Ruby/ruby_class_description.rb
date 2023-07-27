class RubyClassDescription

  attr_accessor :aaa
  def initialize
    @aaa = "1234"
    @bbb = "5678"
  end

  def self.run
    new.run
  end

  def run
    puts @aaa
    puts @bbb
  end

  def test1
    puts @aaa
    puts @bbb
  end

  def test2
    puts test_private_1
    puts test_private_2
  end
  def test4
    puts 00000
  end

  class << self

    ## self 메소드는 외부 호출로 취급받아서 내부의 private를 호출 할 수 없다.
    ## self 메소드는 외부 호출로 취급받아서 내부의 메소도를 호출 할 수 없다.
    ## self 끼리는 호출이 가능하다.
    ## self 메소드 끼리 생성한 클래스 변수는 공유가 가능하다. (연속호출 시)

    def public_value
      @aaa = 1234
      @bbb = 9999
      test1_self
    end
    def test1_self
      puts @aaa
      puts @bbb
    end

    def test3_self
      puts @aaa
      puts @bbb
      puts test_private_1
    end

    def test3
      puts 1246902682038650
      self.test1
    end

    def test_self_3
      puts "aaaaa"
      puts test3
      puts self.test3
    end
  end

  private
  attr_accessor :bbb
  def test_private_1
    puts 1234
    @aaa
  end

  def test_private_2
    puts 1234
    @bbb
  end
end

