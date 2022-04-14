from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *

@config(theme='dark')
def main():
    put_grid([
        [span(put_markdown('## Section A'), col=3)],
        [put_markdown('### Chart 1'), put_markdown('### Chart 2'), put_markdown('### Chart 3')],
        [put_markdown(md), put_scope('1-2'), put_scope('1-3')],
        [span(put_markdown('## Section B'), col=2, row=1), put_markdown('## Section C')],
        [span(put_row([
                put_select('x', help_text='X column', options=['a', 'b']),
                put_select('y', help_text='Y column', options=['x', 'y']),
                ]), col=2, row=1),
            None, 
        ],
        [span(put_image(img_link), col=2, row=1), put_scope('2-3')],
    ], cell_widths='33% 33% 33%')

    with use_scope('1-2'):
        put_html(gdp_chart('animation'))
        
    with use_scope('1-3'):
        put_html(gdp_chart('geo'))
        
    with use_scope('2-3'):
        put_markdown(md)
        put_input('something', label='input something to show as a toast message')
        put_button('submit', onclick=lambda: toast(pin.something))

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)