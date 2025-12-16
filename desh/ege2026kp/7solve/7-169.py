
VImgAfter = 1
kImage = 3840*2160/1280/720
VImgBefore = kImage*VImgAfter
VtotalAfter = VImgAfter + VImgAfter*3
VtotalBefore = VImgBefore + VImgAfter*3

print( VtotalBefore/VtotalAfter )
