import sys
sys.path.insert(0, sys.argv[1])
from make_shape import fillet, write_fitted, to_svg
k = 0.1746  # horizontal shift per pixel of height (skew of the logo)
def lx(y, x0, y0): return x0 - k * (y - y0)
# body: skewed panel with a notch from the top
body = [(686, 625), (716, 625), (716, 1025), (842, 1025), (842, 625), (1141, 625),
        (lx(1167, 1141, 625), 1167), (lx(1167, 686, 625), 1167)]
body = fillet(body, [2, 4, 6, 6, 4, 2, 48, 32])
# cap: skewed band above
cap = [(lx(428, 709, 498), 428), (lx(428, 1164, 498), 428), (1164, 498), (709, 498)]
cap = fillet(cap, [48, 32, 2, 2])
hole = fillet([(887, 715), (1013, 715), (1013, 935), (887, 935)], 6)
contours = [[(x, y) for x, y in c] for c in (body, cap, hole)]
write_fitted(contours, sys.argv[2])
# header mark: same contours, own viewBox
xs=[p[0] for c in contours for p in c]; ys=[p[1] for c in contours for p in c]
x0,y0=min(xs),min(ys)
d=' '.join('M'+' L'.join(f'{x-x0:.1f} {y-y0:.1f}' for x,y in c)+' Z' for c in contours)
open(sys.argv[3],'w').write(f'<svg role="img" viewBox="0 0 {max(xs)-x0:.0f} {max(ys)-y0:.0f}" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" fill-rule="evenodd" d="{d}"/></svg>\n')
