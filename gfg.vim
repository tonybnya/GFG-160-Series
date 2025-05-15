let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/dev
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 GFG-160-Series/001.py
badd +1 GFG-160-Series/input.txt
badd +0 GFG-160-Series/output.txt
argglobal
%argdel
$argadd NvimTree_1
edit GFG-160-Series/001.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 35 + 87) / 174)
exe 'vert 2resize ' . ((&columns * 68 + 87) / 174)
exe '3resize ' . ((&lines * 19 + 21) / 43)
exe 'vert 3resize ' . ((&columns * 69 + 87) / 174)
exe '4resize ' . ((&lines * 20 + 21) / 43)
exe 'vert 4resize ' . ((&columns * 69 + 87) / 174)
argglobal
enew
file NvimTree_1
balt GFG-160-Series/001.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
lcd ~/dev/GFG-160-Series
wincmd w
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 20) / 40)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/dev/GFG-160-Series
wincmd w
argglobal
if bufexists(fnamemodify("~/dev/GFG-160-Series/input.txt", ":p")) | buffer ~/dev/GFG-160-Series/input.txt | else | edit ~/dev/GFG-160-Series/input.txt | endif
if &buftype ==# 'terminal'
  silent file ~/dev/GFG-160-Series/input.txt
endif
balt ~/dev/GFG-160-Series/001.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 9) / 19)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/dev/GFG-160-Series
wincmd w
argglobal
if bufexists(fnamemodify("~/dev/GFG-160-Series/output.txt", ":p")) | buffer ~/dev/GFG-160-Series/output.txt | else | edit ~/dev/GFG-160-Series/output.txt | endif
if &buftype ==# 'terminal'
  silent file ~/dev/GFG-160-Series/output.txt
endif
balt ~/dev/GFG-160-Series/input.txt
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 10) / 20)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/dev/GFG-160-Series
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 35 + 87) / 174)
exe 'vert 2resize ' . ((&columns * 68 + 87) / 174)
exe '3resize ' . ((&lines * 19 + 21) / 43)
exe 'vert 3resize ' . ((&columns * 69 + 87) / 174)
exe '4resize ' . ((&lines * 20 + 21) / 43)
exe 'vert 4resize ' . ((&columns * 69 + 87) / 174)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
