package com.example.parsaniahardik.kotlin_scanxing

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import com.google.zxing.Result
import me.dm7.barcodescanner.zxing.ZXingScannerView
import okhttp3.*
import org.json.JSONObject
import java.io.IOException


class ScanActivity : AppCompatActivity(), ZXingScannerView.ResultHandler {

    var okHttpClient: OkHttpClient = OkHttpClient()

    private var mScannerView: ZXingScannerView? = null

    //hardcode URl.change ip for your own.
    private var URL: String = "http://192.168.1.102:5000//kod_search/gtins/"

    public override fun onCreate(state: Bundle?) {
        super.onCreate(state)
        mScannerView = ZXingScannerView(this)
        setContentView(mScannerView)
    }

    public override fun onResume() {
        super.onResume()
        mScannerView!!.setResultHandler(this)
        mScannerView!!.startCamera()
    }

    public override fun onPause() {
        super.onPause()
        mScannerView!!.stopCamera()
    }

    override fun handleResult(rawResult: Result) {
        // Show type of (qrcode, pdf417 etc.) in log
        //Would necessary when i add difference between gtin and qr
        // Log.v("tag", rawResult.getBarcodeFormat().toString());

        val gtin_url: String = (URL + rawResult.text.toString())
        get_gtin_json(gtin_url)
        onBackPressed()
    }
    private fun get_gtin_json(URL:String) {

        val request: Request = Request.Builder().url(URL).build()
        okHttpClient.newCall(request).enqueue(object : Callback {
            override fun onFailure(call: Call?, e: IOException?) { }

            override fun onResponse(call: Call?, response: Response?) {
                val json = response?.body()?.string()
                // Example from internet how parse json on kotlin. Its work.
                //val first_param = (JSONObject(json).getJSONObject("bpi").getJSONObject("EUR")["rate"] as String).split(".")[0]

                runOnUiThread {
                    MainActivity.tvresult!!.setText(json)
                    //uncoment it after parse json.
                    //MainActivity.tvresult!!.setText(val first_param)
                }
            }
        })
    }
}