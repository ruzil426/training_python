import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
            # print(all_data)

# start = datetime.datetime.now()
# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for i in filenames:
#     read_info(i)
# end = datetime.datetime.now()
# print(end-start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)