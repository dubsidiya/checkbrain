
VImgAfter = 1
kImage = 1920*1080/1280/720
VImgBefore = kImage*VImgAfter
VtotalAfter = VImgAfter + VImgAfter/4
VtotalBefore = VImgBefore + VImgAfter/4

print( VtotalBefore/VtotalAfter )
