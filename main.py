from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    OPERATION_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676204779091&signature=KUsHHiMARxpiApc8lFi8e0BEEz0fIkgDMNM06tCKcSA&downloadName=operations.json"
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data, info = get_data(OPERATION_URL)
    if not data:
        exit(info)
    else:
        print(info)


    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for row in data:
        print(row, end='\n\n')

if __name__ == '__main__':
    main()