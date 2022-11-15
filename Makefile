
.PHONY: install_mssql_driver_on_mac
install_mssql_driver_on_mac:
	# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver16
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
	brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
	brew update
	HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
	sudo ln -s /usr/local/etc/odbcinst.ini /etc/odbcinst.ini
	sudo ln -s /usr/local/etc/odbc.ini /etc/odbc.ini


.PHONY: install_mssql_cli
install_mssql_cli:
	pip install mssql-cli