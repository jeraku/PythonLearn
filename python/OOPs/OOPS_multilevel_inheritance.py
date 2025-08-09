# class Dad:
#     pass
#
#
# class Son(Dad):
#     pass
#
#
# class Grandson(Son):
#     pass
#


class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isdance(self):
        return "I can dance {} no. of times".format(self.dance)


class Grandson(Son):
    dance = 6

    def isdance(self):
        return "Oh Yes, I can dance {} no. of times, check it out!".format(self.dance)


garry = Dad()
harry = Son()
larry = Grandson()

print(larry.dance)
print(larry.isdance())
print(larry.basketball)

