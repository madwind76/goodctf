from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/z':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            # 파일 저장
            with open("post_data.bin", "wb") as f:
                f.write(post_data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data received and saved.\n")
            print(f"Saved {len(post_data)} bytes to post_data.bin")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found\n")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 80)  # 포트는 필요에 따라 수정
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Serving on port {server_address[1]}...")
    httpd.serve_forever()
