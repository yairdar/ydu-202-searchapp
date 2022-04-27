from pywebio import start_server, config
from pywebio.output import *
from pywebio.pin import *

@config(theme='dark')
def main():
    put_grid([
        [span(put_markdown('## Section A'), col=3)],
        [put_markdown('### Chart 1'), put_markdown('### Chart 2'), put_markdown('### Chart 3')],
        [put_markdown('sdf'), put_scope('1-2'), put_scope('1-3')],
        [span(put_markdown('## Section B'), col=2, row=1), put_markdown('## Section C')],
        [span(put_row([
                put_select('x', help_text='X column', options=['a', 'b']),
                put_select('y', help_text='Y column', options=['x', 'y']),
                ]), col=2, row=1),
            None, 
        ],
        [span(put_image('http://'), col=2, row=1), put_scope('2-3')],
    ], cell_widths='33% 33% 33%')

    # with use_scope('1-2'):
    #     put_html(gdp_chart('animation'))
        
    # with use_scope('1-3'):
    #     put_html(gdp_chart('geo'))

    def put_msg(_msg):
        link_html =f'<a href="https://letmegooglethat.com/?q={_msg}">{_msg}</a>'
        with use_scope('1-2'):
            put_html(link_html)     
        
    with use_scope('2-3'):
        put_markdown("sdfdsf")
        put_input('something', label='input something to show as a toast message')
        put_button('submit', onclick=lambda: put_msg("sdf"))

if __name__ == '__main__':
    start_server(main, port=8080, host='0.0.0.0', debug=True, remote_access=True)