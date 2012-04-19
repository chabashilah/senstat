package com.chabashilah.bluetooth_test;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


//ログイン画面
public class LoginActivity extends Activity {
	
	@Override
	public void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(R.layout.login);
		((TextView)findViewById(R.id.email_label)).setText("Email");
		((TextView)findViewById(R.id.password_label)).setText("Password");
		
		//===================UI part===================
		Button button = (Button) findViewById(R.id.login_button);
		// ボタンがクリックされた時に呼び出されるコールバックリスナーを登録します
		button.setOnClickListener(new View.OnClickListener() {
			//@Override
			public void onClick(View v) {
				// ボタンがクリックされた時に呼び出されます
				//Button button = (Button) v;
				//Toast.makeText(Bluetooth_testActivity.this, "onClick()",
						//Toast.LENGTH_SHORT).show();
				Intent intent = new Intent(LoginActivity.this, Bluetooth_testActivity.class);
				startActivity(intent);
			}
		});		
	}
	@Override
	public synchronized void onResume(){
		super.onResume();
		
		
	}
	
}
