vault {
  renew_token = false
  vault_agent_token_file = "/home/vault/.vault-token"
  retry {
    backoff = "1s"
  }
}

template {
  destination = "/etc/secrets/index.html"
  contents = <<EOH
  <html>
  <body>
  <p>Some secrets:</p>
  {{- with secret "secret/data/myapp/config?version=1" }}
  <ul>
  <li><pre>username: {{ .Data.data.username }}</pre></li>
  <li><pre>password: {{ .Data.data.password }}</pre></li>
  </ul>
  <img src="https://www.asphaltandrubber.com/wp-content/uploads/2015/08/Michelin-Man-thumb-up.jpg" alt="W3Schools.com" style="width:350px;height:262px;">
  {{ end }}
  </body>
  </html>
  EOH
}
