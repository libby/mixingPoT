## Silly Simple Script to Collect Input for the Powers of Tau Ceramony
* Running the [Powers of Tau ceremony](https://github.com/ebfull/powersoftau/wiki)
* Uses the [rust client](https://github.com/ebfull/powersoftau)

## [Install the Rust Client](https://www.rust-lang.org/en-US/install.html)
```
$> curl https://sh.rustup.rs -sSf | sh
# add cargo to your $PATH
$> export PATH="$HOME/.cargo/bin:$PATH"
$> git clone https://github.com/ebfull/powersoftau
$> cd powersoftau
$> cargo build
```
## Testing Put `input_capture.py` in powersoftau dir
```
$> cd powersoftau
# create dummy challenge file
$> cargo run --release --bin new
$> python3 input_capture.py
``` 

* Write to the zcash mailing list if you want to run for real.
