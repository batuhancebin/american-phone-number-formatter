import re
def clean_number(number):
    #clean withouth number with regex
    return re.sub(r'\D',"",number)
def clean_country_code(number):
    #clean country code
    if len(number)==10 and number[0]!="1" and number[0]!="0" and number[1]!="0" and number[1]!="1":
        return number
    elif len(number)==11 and number[0]=="1" and number[1]!="0" and number[1]!="1":
        return number[1:]
    elif len(number)==10 and number[0]=="1":
        return None
def format_number(number):
    #format number
    formatted_number=f"({number[:3]}) {number[3:6]}-{number[6:]}"
    return formatted_number
def main():
    user_input= sys.argv[1]
    number = clean_number(user_input)
    number = clean_country_code(number)
    if number is None:
        print("Invalid phone number")
        return
    else:
        formatted_number = format_number(number)
        print(formatted_number)

if __name__ == "__main__":
    main()