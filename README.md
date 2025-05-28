# ⚡ DISCORD TOKEN GENERATOR v1

<p align="center">
  <img src="https://img.shields.io/badge/Status-FREE%20TOOL-green?style=for-the-badge" alt="status" />
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge" alt="platform" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge" alt="language" />
</p>

<p align="center">
  <b>🔥 Advanced Discord Token Generator with Automated Login — FREE edition</b><br>
  🎉 Made with ❤️ by <a href="https://github.com/anomusly">@AnomusLY</a> | Discord Id <a href="https://discord.com/users/1136625769628581928">@Anomus.ly</a>
</p>

---

## ✨ Features

- 🤖 **Automated token extraction** from email:password combinations
- 📧 **Bulk processing** with support for multiple accounts
- 🛡️ **Advanced rate limiting detection** to prevent Discord API blocks
- 🔄 **Automatic retry mechanism** with intelligent backoff
- 📊 **Real-time status updates** with colored console output
- � **Auto-saves tokens** to organized output files
- 🎯 **Email validation** for realistic account processing
- ⚙️ **Enhanced error handling** for robust operation
- 🔄 **Robust logging** with timestamps and status indicators
- 📝 **Multiple output formats** for different use cases

---

## � Installation

```bash
git clone https://github.com/anomusly/Discord-Token-Retriever.git
cd Discord-Token-Retriever
pip install -r requirements.txt
```

### 📋 Requirements

```
requests>=2.31.0
colorama>=0.4.6
termcolor>=2.3.0
pystyle>=2.9
```

---

## 🚀 Usage

### 🎯 Extracting Discord Tokens

1. **Prepare your email list**:
   - Create `emails.txt` in the project directory
   - Add email:password combinations (one per line):
   ```
   example1@gmail.com:password123
   example2@yahoo.com:mypassword
   user@domain.com:secretpass
   ```

2. **Run the token extractor**:
   ```bash
   python main.py
   ```

3. **The tool will automatically**:
   - Validate email formats
   - Process each account with rate limiting
   - Handle Discord API responses
   - Save tokens to multiple output files
   - Display real-time progress with colored output

4. **Check results** in output files:
   - `tokens.txt` - Pure Discord tokens (one per line)
   - `evs.txt` - Complete account data (email:password:token)
   - `output.txt` - Legacy format for compatibility

---

<pre style="color: hotpink; font-weight: bold;">
██████╗ ███████╗███████╗██╗██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝
██║  ██║█████╗  ███████╗██║██████╔╝█████╗
██║  ██║██╔══╝  ╚════██║██║██╔══██╗██╔══╝
██████╔╝███████╗███████║██║██║  ██║███████╗
╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
🚀 Ultimate Discord Token Retriever 🚀
</pre>

## 🧾 Example Usage Flow

1. 📧 **Prepare email:password combinations** in emails.txt
2. 🤖 **Run automated login process** with Discord API
3. 🛡️ **Rate limiting protection** prevents API blocks
4. ✅ **Email validation** ensures proper format
5. 🔑 **Token extraction** via Discord authentication
6. 💾 **Save credentials** to organized output files
7. 📊 **View detailed statistics** of success/failure rates

## ⚙️ Technical Details

| Component | Description | Purpose |
|-----------|-------------|---------|
| `Discord API v9` | Authentication endpoint | Token extraction |
| `Rate Limiting` | 3-second delays + 429 handling | Prevent blocks |
| `Email Validation` | Regex pattern matching | Input validation |
| `Multi-format Output` | tokens.txt, evs.txt, output.txt | Organized results |
| `Error Handling` | Try-catch with logging | Robust operation |

## 🎯 Automation Features

- 🔄 **Continuous processing** loop for multiple accounts
- 🛡️ **Rate limit detection** and automatic waiting (60s for 429 errors)
- 📧 **Email format validation** with regex patterns
- 🎲 **Intelligent error handling** for network/API issues
- 🔍 **Smart response parsing** with detailed status codes
- 💻 **Cross-platform compatibility** (Windows/Linux/macOS)
- ⏳ **Built-in delays** (3 seconds between requests)

## ⚠️ Important Notes

- 🚦 **Rate limiting is automatically handled** to prevent blocks
- 📧 **Only works with valid Discord accounts** that have tokens
- 🔄 **Automatic retry on rate limits** with 60-second delays
- 📊 **All tokens are automatically saved** to multiple files
- 🎯 **Email validation prevents invalid requests**
- ⚖️ **Use responsibly** and follow Discord's Terms of Service

## 🛠️ Troubleshooting

### Common Issues:
- **"emails.txt not found"**: Create the file with email:password combinations
- **"Invalid email format"**: Ensure emails follow proper format (user@domain.com)
- **"Rate limited"**: Tool automatically waits 60 seconds and retries
- **"Invalid credentials"**: Check if email:password combinations are correct

### Solutions:
- Ensure emails.txt exists in the same directory as main.py
- Check email:password format (use colon separator)
- Verify internet connection for API requests
- Run as administrator if file permission issues occur

## � Support Development

If this tool saved you time or helped you out, feel free to donate 💰:

**Litecoin (LTC)**: `ltc1qrw6ns4sxcngy9mjz8u96kn25clks858lwgtarr`

## 📞 Contact & Support

- 💬 **Discord**: `anomus.ly`
- 🛠️ **Custom Tools**: DM me on Discord with details and budget
- � **Issues**: Open an issue on GitHub

---

<p align="center">
  <b>⭐ If this tool helped you, please give it a star! ⭐</b>
</p>

## ⚖️ Disclaimer

This tool is for educational purposes only. Users are responsible for complying with Discord's Terms of Service and applicable laws. The developer is not responsible for any misuse of this software.

