from textual.widgets import Welcome
from textual.app import App, ComposeResult


class MyApp(App):
    pass

    def mount(self, *widgets, before=None, after=None):
        pass
        
    #def compose(self) -> ComposeResult:
        #pass
    
    def compose(self) -> ComposeResult:
        yield Welcome()

    
    
if __name__ == "__main__":
    app = MyApp()
    app.run()