package com.teamproject.main;

import com.teamproject.controller.AuthController;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class MainApp extends Application {

    
	 public void start(Stage primaryStage) {
	        showMainPage(primaryStage);
	    }
    public void showMainPage(Stage primaryStage) {
        primaryStage.setTitle("Main Application");

        // 主界面布局
        VBox layout = new VBox(10);
        layout.setStyle("-fx-padding: 20; -fx-alignment: center;");

        // 按钮：导航到不同的功能
        Button registerButton = new Button("Register");
        Button loginButton = new Button("Login");
        Button adminButton= new Button("admin");
        Button exitButton = new Button("Exit");
        
       
        registerButton.setOnAction(e -> showRegisterPage(primaryStage));
        loginButton.setOnAction(e -> showLoginPage(primaryStage));
        adminButton.setOnAction(e -> showadminPage(primaryStage));
        exitButton.setOnAction(e -> primaryStage.close());
       

        // 将按钮添加到布局中
        layout.getChildren().addAll(new Label("Welcome to the Main Application"), registerButton, loginButton, exitButton,adminButton);

        // 设置主场景
        primaryStage.setScene(new Scene(layout, 800, 400));
        primaryStage.show();
    }

    private void showRegisterPage(Stage primaryStage) {
        VBox registerLayout = new VBox(10);
        registerLayout.setStyle("-fx-padding: 20; -fx-alignment: center;");

        TextField usernameField = new TextField();
        usernameField.setPromptText("Enter username");

        TextField emailField = new TextField();
        emailField.setPromptText("Enter email");

        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Enter password");

        Button registerButton = new Button("Register");
        Button backButton = new Button("Back");
        Label resultLabel = new Label();
        
        registerButton.setOnAction(e -> {
            String username = usernameField.getText();
            String email = emailField.getText();
            String password = passwordField.getText();

            String result = AuthController.registerUser(username, email, password);
            resultLabel.setText(result);
        });
        
        backButton.setOnAction(e -> showMainPage(primaryStage));
        registerLayout.getChildren().addAll(new Label("Register"), usernameField, emailField, passwordField, registerButton, resultLabel,backButton);
        primaryStage.setScene(new Scene(registerLayout, 800, 400));
    }

    private void showLoginPage(Stage primaryStage) {
        VBox loginLayout = new VBox(10);
        loginLayout.setStyle("-fx-padding: 20; -fx-alignment: center;");

        TextField usernameField = new TextField();
        usernameField.setPromptText("Enter username");

        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Enter password");

        Button loginButton = new Button("Login");
        Button backButton = new Button("Back");
        Label resultLabel = new Label();

        loginButton.setOnAction(e -> {
            String username = usernameField.getText();
            String password = passwordField.getText();

            String result = AuthController.loginUser(username, password);
            resultLabel.setText(result);
        });
        backButton.setOnAction(e -> showMainPage(primaryStage));
        loginLayout.getChildren().addAll(new Label("Login"), usernameField, passwordField, loginButton, resultLabel,backButton);
        primaryStage.setScene(new Scene(loginLayout, 800, 400));
    }
    private void showadminPage(Stage adminStage)
    {
    	   VBox loginLayout = new VBox(10);
           loginLayout.setStyle("-fx-padding: 20; -fx-alignment: center;");

           TextField usernameField = new TextField();
           usernameField.setPromptText("Enter username");
           
    }

    public static void main(String[] args) {
        launch(args);
    }
    
}
