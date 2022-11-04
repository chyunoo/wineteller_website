mkdir -p ~/.streamlit/

echo "\n\
[general]\n\
email = \"your-email@domain.com\"\n\
" >> ~/.streamlit/credentials.toml

echo "\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
\n\
[theme]\n\
primaryColor = '#722f37'\n\
backgroundColor = '#37474f'\n\
textColor = '#white'\n\
secondaryBackgroundColor = '#841f27'\n\
" > ~/.streamlit/config.toml
