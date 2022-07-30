mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#4BFFF6'
backgroundColor = '#073B24'
secondaryBackgroundColor = '#262730'
textColor= '#C9B7B7'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml