import os
from winotify import Notification
from config.logging import LOG_FILENAME


def success():
    notification = Notification(
        app_id='TiqueTaque Marker',
        title='Finalizado',
        msg='O ponto foi registrado com sucesso!'
    )

    return notification


def failed():
    notification = Notification(
        app_id='TiqueTaque Marker',
        title='Erro',
        msg='NÃO foi possível realizar o registro do ponto...'
    )
    
    notification.add_actions(
        label='Ver error',
        launch=f'{os.path.abspath(LOG_FILENAME)}'
    )

    return notification
