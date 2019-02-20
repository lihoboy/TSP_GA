def main():
    try:
        import threading

        print(threading.current_thread())

        run()



    except ImportError:
        import dummy_threading as threading
def run():
    product_i=1
    for i in range (1,5000):
        product_i*=i
        for j in range(i):
            product_i+=j
    print(product_i)

if __name__ == "__main__":
    # execute only if run as a script
    main()
