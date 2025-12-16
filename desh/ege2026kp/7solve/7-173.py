
VImgAfter = 1
kImage = 3840*2160*32/1920/1080/16
VImgBefore = kImage*VImgAfter
VAudioBefore = VImgAfter/2
VAudioAfter = VAudioBefore/4

VtotalAfter = VImgAfter + VAudioAfter
VtotalBefore = VImgBefore + VAudioBefore

print( VtotalBefore/VtotalAfter )
