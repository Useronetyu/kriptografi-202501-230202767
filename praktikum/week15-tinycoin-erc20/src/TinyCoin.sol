// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import standar ERC20 dari OpenZeppelin
// (URL ini memungkinkan Remix IDE untuk mengambil kode langsung dari GitHub)
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    /**
     * @dev Constructor ini akan dipanggil satu kali saat kontrak di-deploy.
     * @param initialSupply Jumlah token awal yang ingin dicetak (misal: 1000).
     */
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        // _mint adalah fungsi internal OpenZeppelin untuk mencetak token baru.
        // msg.sender = Alamat dompet yang melakukan deployment (kamu).
        // dikali 10^18 karena standar desimal ERC20 adalah 18 digit.
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }
}