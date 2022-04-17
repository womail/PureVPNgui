#import PySimpleGUIQt as sg  
import subprocess
import os
from nicegui import ui
from datetime import datetime
import random
import string
letters = string.ascii_lowercase

def setvariables():
    status_vars=[]
    cmd="purevpn --info"
    message = subprocess.check_output(cmd, shell=True)
    
    msg= message.decode() #decode bytes to str

    textlist=msg.split("\n")    # parse the text
                                # IP Address is 4
                                # Country is 5
    status_vars.append (str(textlist[4]))
    status_vars.append (str(textlist[5]))

    cmd="purevpn --status"
    message = subprocess.check_output(cmd, shell=True)
    msg= message.decode() #decode bytes to str
    textlist=msg.split(" ")
 
    if textlist[3] == "Not":
        status_vars.append("Not Connected")
    else:
         status_vars.append("Connected")
    return status_vars
    
status = setvariables()



def button_vpnstatus():
    status = setvariables()
  
    ui.notify(f"Status : {status[2]} in {status[1]}")

def btn_disp_info():
 
    global disp_status
    global disp_location
    global disp_ipaddr
#
    status = setvariables()
    disp_statusx=( ''.join(random.choice(letters) for i in range(10)) )
    disp_status=status[2]
    disp_location=status[0]
    disp_ipaddr=status[1]
    button_result1.set_text(f'Status:     {disp_status}')
    button_result2.set_text(f"Location:   {disp_location}")
    button_result3.set_text(f"IP Address:   {disp_ipaddr}")    

def button_startvpn():
    os.system("purevpn --connect")
    btn_disp_info()
    
def button_switchvpn():
    os.system("purevpn --disconnect")
    os.system("purevpn --connect")
    btn_disp_info()

def button_stopvpn():
    os.system("purevpn --disconnect")
    btn_disp_info()

def btn_show_locations():
    with ui.page('/locations'):
        ui.label('Welcome to the other side')
        ui.link('Back to main page', '/')
    ui.link('See Locations', '/locations')

def toggle_connect(country_code):
    os.system(f"purevpn --disconnect ")
    ui.notify("Connecting to {}...".format(country_code))
    os.system(f"purevpn --connect {country_code}")
    ui.notify("Connected to {}...".format(country_code))
    btn_disp_info()

with ui.row():
    base64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAMAAABrrFhUAAACZ1BMVEUAAAD////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////6+vr///9EuxJPxRVvz0Cw45ZIvBb1+fPj9Nz0/PBGvRT5+/n6/vlKvhj9//xQwCDw9+zl896F113t9ulRxhjD67BXwylNvxxUxxve8dVXyB/3/PTx+u3r9ubI7LZgyytdySdSwSPn99/b88/V8ci95a15001vy0hhxjZjzC+n3pGm4Yqf3oKT2nKJ02ljyDhVwiXy+PDv+urq9+PN68GV3HN4z1Ps+ebS7cfM7bvA6ayY23qU13iA0F57z1dyzE1rykJnxz9qzjpZwyv3+fbp9eTn9OHh9djF6ba96ai656Wr4pCk3Iyd3n6O1XCJ12aB1lh91FJ10kdoyj1nzTVdxTDq+OPg8tnZ787C5rG556K25p+z5pqd2oSQ1nN1zk5ZySPe9NTb8NHR7sPH6bm86Kaw4Zyp4o2Y2H2b3nmQ2m6N2WiE0mSH1mJy0ENlzTP4+fet4Zaj4YWC017X783O7sC246Or35WM12x/0lltzz265Kiu5JPS8MNgxzNcxS1gmY7UAAAATXRSTlMA+k/wA7v1BcdIAScx7tp8VTsJ98+adDYsHxjLtbElFhMH/Onj3dTAjIWAPy6hbBvDfmZMQuy4rqmUkXBcDeXgeWnypJ1goGK9jovRKrljprYAABKHSURBVHja5Nz5XxZFHMDxgUCsFFEEBTOSQ+RKDTMltMujfpjvDD5ccoNcCirIIQhIgCgICJogR0qeaB6peR9Rppn1TwVl2Dy7zzMzO/voPvb+D/bzWmZnvzsP6NUImRH/WdS6lXPDQkPD5q5cF/W+54wQ9D/gFRSzMSruS19/0OHv+2Vc1MaYIC/0GloT6/nx6pW+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'
    ui.image(base64).style('width:180px')
    with ui.card():
        ui.label('PureVPN Control Panel').classes('text-h5')
        
        with ui.row():
            with ui.column():
                #with ui.row():
                ui.button('Connect to VPN', on_click=button_startvpn)
                ui.button('Disconnect  VPN ', on_click=button_stopvpn)
                ui.button('Check VPN status', on_click=btn_disp_info)
                ui.button('View VPN Locations', on_click=btn_show_locations)
                with ui.card():
                    with ui.column():
                        button_result1 = ui.label('Status:     -------------')
                    with ui.column():
                        button_result2 = ui.label('Location:   -------------')
                    with ui.column():
                        button_result3 = ui.label('IP Address: -------------')
                        btn_disp_info()
                    ui.button('VPN Killswitch', on_click=button_stopvpn).props('inline color=red')
            
                with ui.card():
                        #ui.label('Current Time').classes('text-h6')
                        with ui.row():
                            ui.icon('far fa-clock')
                            clock = ui.label()
                            t = ui.timer(0.1, lambda: clock.set_text(datetime.now().strftime("%X")))

                # with ui.card():
        
    with ui.card():
        ui.label('VPN Connection Locations').classes('text-h6')
        ui.label("By clicking a region, the toggle will disconnect your ")  
        ui.label("current location and reconnect to the new location")
        with ui.column():
            with ui.row():   
                ui.label('Select a Location:').classes('text-bold')
                output = ui.label('').classes('text-bold')  
            with ui.row():
                toggle = ui.toggle(["IE", "UK", "US", "FR"], value="UK", on_change=lambda e: toggle_connect(e.value),)
    with ui.card():
        with ui.card():
            with ui.card():

        #with ui.column():
        #    'ui.label('Ststemctl commands').classes('text-h5')
        #    'ui.label('sudo systemctl status purevpn         ').classes('text-h6')
                ui.markdown('### Headline\nWith **hyperlink** to `[GitHub](https://github.com/zauberzeug/nicegui`).')
                ui.markdown('|Option|Commands to run |')
                ui.markdown('|--|--|')
                ui.markdown('| Check service status |`sudo  systemctl status purevpn`  |')
                ui.markdown('|Start PureVPN Service|`sudo  systemctl status purevpn`|')
                ui.markdown('| Enable PureVPN Service | `sudo  systemctl enable --now purevpn` |')
                ui.markdown('|Stop PureVPN Service|sudo  systemctl stop purevpn|')
    button_count = 0
    
ui.run()
