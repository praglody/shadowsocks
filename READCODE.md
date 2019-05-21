### EventLoop

- `self._fdmap`
    
    { f.fileno(): (f, handler), }
    
    这是一个字典，key 是 sock 句柄的值，value 是一个句柄和handler对象组成的元组
    
    `通过 [TCPRelay.add_to_loop() -> self._eventloop.add()] 和 [TCPRelay.handle_event() -> TCPRelayHandler() -> self._loop.add()] 两种方式添加值`

    ```
    def add(self, f, mode, handler):
        fd = f.fileno()
        self._fdmap[fd] = (f, handler)
        self._impl.register(fd, mode)
    ```

### TCPRelay & TCPRelayHandler

- `self._fd_to_handlers`
    
    这个里面存储绑定了 sock 的 TCPRelayhandler

    ```
    self._fd_to_handlers[local_sock.fileno()] = self
    
    self._fd_to_handlers[remote_sock.fileno()] = self
    ```
    

```
TCPRelay 和 TCPRelayHandler 的 _fd_to_handlers 属性是同一个对象，通过引用赋值

- TCPRelay._fd_to_handlers
- TCPRelayHandler._fd_to_handlers

```
