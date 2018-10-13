class Masking:
    def email_masking(self, email):
        data = email.split("@")
        first = data[0][0]
        last = data[0][len(data[0])-1]
        return first + "*****" + last + "@" + data[1]

    def phone_masking(self, phone):
        num_count = 0        
        phone_ar = list(phone)
        for i in range(len(phone_ar)):
            if phone_ar[i].isdigit() and num_count < 6:
                phone_ar[i] = "*"
                num_count += 1
        return ''.join(phone_ar)

def main():
    mask = Masking()
    print(mask.email_masking("hello@gmail.com"))
    print(mask.phone_masking("(510)579-9029"))

main()

        


    