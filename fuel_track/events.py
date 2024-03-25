# events.py

class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name, callback):
        if event_name in self.listeners and callback in self.listeners[event_name]:
            self.listeners[event_name].remove(callback)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(*args, **kwargs)

# Creamos una instancia global de EventManager
event_manager = EventManager()

# Definimos funciones convenientes para suscribirnos, cancelar la suscripción y emitir eventos
subscribe = event_manager.subscribe
unsubscribe = event_manager.unsubscribe
emit = event_manager.emit
