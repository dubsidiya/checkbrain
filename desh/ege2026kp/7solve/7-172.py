
VImgAfter = 1
kImage = 3840*2160/1920/1080
VImgBefore = kImage*VImgAfter
VAudioBefore = 2*VImgAfter
VAudioAfter = VAudioBefore/2

VtotalAfter = VImgAfter + VAudioAfter
VtotalBefore = VImgBefore + VAudioBefore

print( VtotalBefore/VtotalAfter )
