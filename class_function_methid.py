class earth:
    def life(n):
        return n * 5
class mass:
    def gravity(n):
        return n * 10
    
def main():
    input = 5
    first_out = earth.life(input)
    second_out = mass.gravity(first_out)
    print(first_out)
    print(second_out)

if __name__ == "__main__":
    main()