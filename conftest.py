import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    print(r""" 
 ____  _     _  __ _     ____                       _ _         
/ ___|| |__ (_)/ _| |_  / ___|  ___  ___ _   _ _ __(_) |_ _   _ 
\___ \| '_ \| | |_| __| \___ \ / _ \/ __| | | | '__| | __| | | |
 ___) | | | | |  _| |_   ___) |  __/ (__| |_| | |  | | |_| |_| |
|____/|_| |_|_|_|  \__| |____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                          |___/                                                                                        
                            SHIFT SECURITY TEST SUITE 🚀
""")


