let saldo = 1000;

while (opcao !== 4) {
    opcao = Number(prompt("=== MENU BANCO ===\n1 - Ver Saldo\n2 - Depositar\n3 - Sacar\n4 - Sair\nEscolha uma opção:"));

    if (opcao === 1) {
        alert("Seu saldo atual é: R$ " + saldo.toFixed(2));
    } else if (opcao === 2) {
        let deposito = Number(prompt("Digite o valor para depositar:"));
        if (deposito > 0) {
            saldo += deposito;
            alert("Depósito realizado! Saldo atual: R$ " + saldo.toFixed(2));
        } else {
            alert("Valor inválido para depósito!");
        }
    } else if (opcao === 3) {
        let saque = Number(prompt("Digite o valor para sacar:"));
        if (saque > 0 && saque <= saldo) {
            saldo -= saque;
            alert("Saque realizado! Saldo atual: R$ " + saldo.toFixed(2));
        } else {
            alert("Saldo insuficiente ou valor inválido!");
        }
    } else if (opcao === 4) {
        alert("Obrigado por usar nosso banco!");
    } else {
        alert("Opção inválida! Tente novamente.");
    }
}